import React, { useEffect, useState } from "react";
import { Grid, Box, Paper, Typography, Button } from "@mui/material";
import { useNavigate } from "react-router-dom";
import CardTurma, { Turma } from "../components/CardTurma";
import CardMaterial, { Material } from "../components/CardMaterial";
import CardAula, { Aula } from "../components/CardAula";
import { buscarTurmas } from "../services/turmaService";
import { buscarMateriais } from "../services/materialService";
import { buscarAulas } from "../services/aulaService";
import Header from "../components/Header";
import Sidebar from "../components/Sidebar";

const DashboardProfessor: React.FC = () => {
  const [turmas, setTurmas] = useState<Turma[]>([]);
  const [materiais, setMateriais] = useState<Material[]>([]);
  const [aulas, setAulas] = useState<Aula[]>([]);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  // Ajuste para pegar nome/email/foto do localStorage/contexto
  const userName = localStorage.getItem("nome") || "Professor";
  const userEmail = localStorage.getItem("userEmail") || "";
  const userFoto = localStorage.getItem("userFoto");

  const handleLogout = () => {
    localStorage.clear();
    navigate("/login");
  }

  useEffect(() => {
    const fetchData = async () => {
      setLoading(true);
      setTurmas(await buscarTurmas());
      setMateriais(await buscarMateriais());
      setAulas(await buscarAulas());
      setLoading(false);
    };
    fetchData();
  }, []);

  if (loading) return <Box p={4}><Typography>Carregando...</Typography></Box>;

  return (
    <Box sx={{ display: "flex" }}>
      <Sidebar nome={userName} email={userEmail} fotoUrl={userFoto || undefined} onLogout={handleLogout} />
      <Box sx={{ flexGrow: 1 }}>
        <Header nome={userName} />
        <Box p={4}>
          <Grid container spacing={3} justifyContent="center">
            {/* TURMAS */}
            <Grid item xs={12} md={6}>
              {turmas.length === 0 ? (
                <Paper elevation={6} sx={{ p: 3, borderRadius: 3, mb: 3 }}>
                  <Box textAlign="center">
                    <Typography variant="h6">Nenhuma turma cadastrada!</Typography>
                    <Button
                      variant="contained"
                      color="primary"
                      sx={{ mt: 2 }}
                      onClick={() => navigate('/nova-turma')}
                    >
                      Adicionar Turma
                    </Button>
                  </Box>
                </Paper>
              ) : (
                turmas.slice(-3).reverse().map(turma => (
                  <Box key={turma.id} mb={2}>
                    <CardTurma
                      turma={turma}
                      onEdit={() => alert("Editar turma")}
                      onDelete={() => alert("Excluir turma")}
                      onView={() => alert("Detalhes da turma")}
                    />
                  </Box>
                ))
              )}
            </Grid>
            {/* MATERIAIS */}
            <Grid item xs={12} md={6}>
              {materiais.length === 0 ? (
                <Paper elevation={6} sx={{ p: 3, borderRadius: 3, mb: 3 }}>
                  <Box textAlign="center">
                    <Typography variant="h6">Nenhum material cadastrado!</Typography>
                    <Button
                      variant="contained"
                      color="primary"
                      sx={{ mt: 2 }}
                      onClick={() => navigate('/novo-material')}
                    >
                      Adicionar Material
                    </Button>
                  </Box>
                </Paper>
              ) : (
                materiais.slice(-3).reverse().map(material => (
                  <Box key={material.id} mb={2}>
                    <CardMaterial
                      material={material}
                      onEdit={() => alert("Editar material")}
                      onDelete={() => alert("Excluir material")}
                      onView={() => alert("Detalhes do material")}
                      onDownload={() => window.open(material.arquivo_url, "_blank")}
                    />
                  </Box>
                ))
              )}
            </Grid>
            {/* AULAS */}
            <Grid item xs={12} md={6}>
              {aulas.length === 0 ? (
                <Paper elevation={6} sx={{ p: 3, borderRadius: 3, mb: 3 }}>
                  <Box textAlign="center">
                    <Typography variant="h6">Nenhuma aula cadastrada!</Typography>
                    <Button
                      variant="contained"
                      color="primary"
                      sx={{ mt: 2 }}
                      onClick={() => navigate('/nova-aula')}
                    >
                      Adicionar Aula
                    </Button>
                  </Box>
                </Paper>
              ) : (
                aulas.slice(-3).reverse().map(aula => (
                  <Box key={aula.id} mb={2}>
                    <CardAula
                      aula={aula}
                      onEdit={() => alert("Editar aula")}
                      onDelete={() => alert("Excluir aula")}
                      onView={() => alert("Detalhes da aula")}
                    />
                  </Box>
                ))
              )}
            </Grid>
          </Grid>
        </Box>
      </Box>
    </Box>
  );
};

export default DashboardProfessor;