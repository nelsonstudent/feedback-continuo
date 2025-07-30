import React from "react";
import { Paper, Typography, Button, Box } from "@mui/material";

interface CardMensagemProps {
  mensagem: string;
  onClick: () => void;
  labelBotao: string;
}

const CardMensagem: React.FC<CardMensagemProps> = ({ mensagem, onClick, labelBotao }) => (
  <Paper elevation={6} sx={{ p: 3, mb: 3, maxWidth: 400, mx: "auto" }}>
    <Box textAlign="center">
      <Typography variant="h6" gutterBottom>{mensagem}</Typography>
      <Button variant="contained" color="primary" onClick={onClick}>{labelBotao}</Button>
    </Box>
  </Paper>
);

export default CardMensagem;