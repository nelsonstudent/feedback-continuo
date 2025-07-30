import React from "react";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import Login from "./pages/Login";
import Register from "./pages/Register";
import DashboardProfessor from "./pages/DashboardProfessor";
import FormTurma from "./pages/forms/FormTurma";
import FormMaterial from "./pages/forms/FormMaterial";
import FormAula from "./pages/forms/FormAula";

// Telas futuras: dashboard-aluno, dashboard-professor, etc.
const Placeholder = ({ title }: { title: string }) => (
  <div style={{ padding: 40 }}>
    <h2>{title}</h2>
    <p>Página em construção.</p>
  </div>
);

export default function AppRoutes() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/cadastro" element={<Register />} />
        <Route path="/dashboard-aluno" element={<Placeholder title="Dashboard Aluno" />} />
        <Route path="/dashboard-professor" element={<DashboardProfessor />} />
        <Route path="/nova-turma" element={<FormTurma />} />
        <Route path="/novo-material" element={<FormMaterial />} />
        <Route path="/nova-aula" element={<FormAula />} />
        <Route path="/esqueci-senha" element={<Placeholder title="Recuperar senha" />} />
        <Route path="/" element={<Navigate to="/login" replace />} />
        <Route path="*" element={<div>Página não encontrada</div>} />
      </Routes>
    </BrowserRouter>
  );
}