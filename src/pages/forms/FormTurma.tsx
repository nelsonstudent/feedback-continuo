import React, { useState } from "react";
import { Box, Button, TextField, Typography } from "@mui/material";
import { useNavigate } from "react-router-dom";
import { criarTurma } from "../../services/turmaService";

const FormTurma: React.FC = () => {
  const [codigoTurma, setCodigoTurma] = useState("");
  const [mentorId, setMentorId] = useState("");
  const [mentorNome, setMentorNome] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    await criarTurma({
      codigo_turma: codigoTurma,
      mentor: {
        id: Number(mentorId),
        nome: mentorNome,
      },
    });
    navigate("/dashboard-professor");
  };

  return (
    <Box maxWidth={400} mx="auto" mt={4}>
      <Typography variant="h5" mb={2}>Cadastrar Turma</Typography>
      <form onSubmit={handleSubmit}>
        <TextField
          label="Código da Turma"
          value={codigoTurma}
          onChange={e => setCodigoTurma(e.target.value)}
          fullWidth
          required
          margin="normal"
        />
        <TextField
          label="ID do Mentor"
          value={mentorId}
          onChange={e => setMentorId(e.target.value)}
          fullWidth
          required
          margin="normal"
        />
        <TextField
          label="Nome do Mentor"
          value={mentorNome}
          onChange={e => setMentorNome(e.target.value)}
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

export default FormTurma;