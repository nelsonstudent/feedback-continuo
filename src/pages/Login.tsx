import React, { useState } from "react";
import Grid from "@mui/material/Grid";
import { Avatar, Button, TextField, Link, Box, Typography, Paper, Alert, CircularProgress } from "@mui/material";
import LockOutlinedIcon from "@mui/icons-material/LockOutlined";
import { useNavigate, Link as RouterLink } from "react-router-dom";
import { login } from "../services/authService";
import { LoginPayload } from "../types";

const initialState: LoginPayload = { email: "", senha: "" };

export default function Login() {
  const navigate = useNavigate();
  const [form, setForm] = useState(initialState);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    try {
      const res = await login(form);
      localStorage.setItem("token", res.access_token);
      localStorage.setItem("role", res.role);
      localStorage.setItem("nome", res.nome);
      localStorage.setItem("id", String(res.id));
      if (res.role === "professor") {
        navigate("/dashboard-professor");
      } else {
        navigate("/dashboard-aluno");
      }
    } catch (err: any) {
      setError(
        err?.response?.data?.msg ||
          "Erro ao tentar fazer login. Por favor, verifique suas credenciais."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <Grid container component="main" sx={{ height: "100vh" }}>
      {/* Lado esquerdo: informações/branding */}
      <Grid
        item
        xs={12}
        sm={6}
        md={7}
        sx={{
          background: "linear-gradient(120deg, #e3f2fd 50%, #fff 100%)",
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
          alignItems: "center",
          p: 4,
        }}
      >
        <Box sx={{ maxWidth: 420 }}>
          <Typography variant="h3" gutterBottom color="primary" fontWeight={700}>
            SIAS
          </Typography>
          <Typography variant="h6" gutterBottom>
            Sistema de Avaliação Simultânea
          </Typography>
          <Typography sx={{ mt: 4 }}>
            • Acompanhe seu progresso e participação.<br />
            • Professores compartilham materiais e avaliam.<br />
            • Feedback contínuo para evolução no ensino.
          </Typography>
        </Box>
      </Grid>

      {/* Lado direito: formulário de login */}
      <Grid
        item
        xs={12}
        sm={6}
        md={5}
        component={Paper}
        elevation={6}
        square
        sx={{
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
        }}
      >
        <Box
          sx={{
            my: 6,
            mx: 4,
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            width: "100%",
            maxWidth: 360,
          }}
        >
          <Avatar sx={{ m: 1, bgcolor: "primary.main" }}>
            <LockOutlinedIcon />
          </Avatar>
          <Typography component="h1" variant="h5">
            Entrar no SIAS
          </Typography>
          <Box
            component="form"
            onSubmit={handleSubmit}
            sx={{ mt: 1, width: "100%" }}
          >
            <TextField
              margin="normal"
              required
              fullWidth
              id="email"
              label="E-mail"
              name="email"
              autoComplete="email"
              autoFocus
              value={form.email}
              onChange={handleChange}
            />
            <TextField
              margin="normal"
              required
              fullWidth
              name="senha"
              label="Senha"
              type="password"
              id="senha"
              autoComplete="current-password"
              value={form.senha}
              onChange={handleChange}
            />
            <Grid container>
              <Grid item xs>
                <Link component={RouterLink} to="/esqueci-senha" variant="body2">
                  Esqueci minha senha
                </Link>
              </Grid>
            </Grid>
            {error && (
              <Alert severity="error" sx={{ mt: 2 }}>
                {error}
              </Alert>
            )}
            <Button
              type="submit"
              fullWidth
              variant="contained"
              color="primary"
              sx={{ mt: 3, mb: 2 }}
              disabled={loading}
            >
              {loading ? <CircularProgress size={24} color="inherit" /> : "Entrar"}
            </Button>
            <Grid container justifyContent="center">
              <Grid item>
                <Typography variant="body2">
                  Não tem conta?{" "}
                  <Link component={RouterLink} to="/cadastro">
                    Cadastre-se
                  </Link>
                </Typography>
              </Grid>
            </Grid>
          </Box>
        </Box>
      </Grid>
    </Grid>
  );
}