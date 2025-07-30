import React from "react";
import Sidebar from "./Sidebar";
import Header from "./Header";
import Box from "@mui/material/Box";

type LayoutProfessorProps = {
  children: React.ReactNode;
  nome: string;
  email?: string;
  fotoUrl?: string;
  onLogout?: () => void;
};

const LayoutProfessor: React.FC<LayoutProfessorProps> = ({
  children,
  nome,
  email,
  fotoUrl,
  onLogout,
}) => (
  <Box sx={{ display: "flex" }}>
    <Sidebar nome={nome} email={email} fotoUrl={fotoUrl} onLogout={onLogout} />
    <Box sx={{ flexGrow: 1 }}>
      <Header nome={nome} />
      <Box p={4}>{children}</Box>
    </Box>
  </Box>
);

export default LayoutProfessor;