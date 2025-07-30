import React, { useState } from "react";
import { Box, Button, TextField, Typography } from "@mui/material";
import { useNavigate } from "react-router-dom";
import { criarAula } from "../../services/aulaService";

const FormAula: React.FC = () => {
  const [tema, setTema] = useState("");
  const [data, setData] = useState(""); // novo campo
  const [grupoAulaId, setGrupoAulaId] = useState(""); // novo campo
  const navigate = useNavigate();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    await criarAula({
      tema,
      data,
      grupo_aula_id: Number(grupoAulaId), // se for number, ajuste conforme necessário
    });
    navigate("/dashboard-professor");
  };

  return (
    <Box maxWidth={400} mx="auto" mt={4}>
      <Typography variant="h5" mb={2}>Cadastrar Aula</Typography>
      <form onSubmit={handleSubmit}>
        <TextField
          label="Tema da Aula"
          value={tema}
          onChange={e => setTema(e.target.value)}
          fullWidth
          required
          margin="normal"
        />
        <TextField
          label="Data"
          type="date"
          value={data}
          onChange={e => setData(e.target.value)}
          fullWidth
          required
          margin="normal"
          InputLabelProps={{ shrink: true }}
        />
        <TextField
          label="ID do Grupo da Aula"
          value={grupoAulaId}
          onChange={e => setGrupoAulaId(e.target.value)}
          fullWidth
          required
          margin="normal"
        />
        <Button type="submit" variant="contained" color="primary" fullWidth>
          Salvar
        </Button>
      </form>
    </Box>
  );
};

export default FormAula;