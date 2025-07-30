import React, { useState } from "react";
import { Box, Button, TextField, Typography } from "@mui/material";
import { useNavigate } from "react-router-dom";
import { criarMaterial } from "../../services/materialService";

const FormMaterial: React.FC = () => {
  const [nome, setNome] = useState("");
  const [arquivo, setArquivo] = useState<File | null>(null);
  const navigate = useNavigate();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append("nome", nome);
    if (arquivo) formData.append("arquivo", arquivo);
    await criarMaterial(formData);
    navigate("/dashboard-professor");
  };

  return (
    <Box maxWidth={400} mx="auto" mt={4}>
      <Typography variant="h5" mb={2}>Cadastrar Material</Typography>
      <form onSubmit={handleSubmit}>
        <TextField
          label="Nome do Material"
          value={nome}
          onChange={e => setNome(e.target.value)}
          fullWidth
          required
          margin="normal"
        />
        <Button
          variant="contained"
          component="label"
          fullWidth
          sx={{ my: 2 }}
        >
          Selecionar Arquivo
          <input
            type="file"
            hidden
            onChange={e => setArquivo(e.target.files?.[0] || null)}
          />
        </Button>
        <Button type="submit" variant="contained" color="primary" fullWidth>
          Salvar
        </Button>
      </form>
    </Box>
  );
};

export default FormMaterial;