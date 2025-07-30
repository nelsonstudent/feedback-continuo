import React from "react";
import { AppBar, Toolbar, Typography, Box } from "@mui/material";

const Header: React.FC<{ nome?: string }> = ({ nome }) => (
  <AppBar position="static" color="primary" elevation={2}>
    <Toolbar>
      <Typography variant="h6" sx={{ flexGrow: 1 }}>
        {nome ? `Bem-vindo, ${nome}!` : "Bem-vindo!"}
      </Typography>
      {/* Aqui você pode colocar avatar, logout, etc */}
    </Toolbar>
  </AppBar>
);

export default Header;