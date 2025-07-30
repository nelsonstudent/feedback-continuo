import React, { useState } from "react";
import Grid from "@mui/material/Grid";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import Paper from "@mui/material/Paper";
import {
  Avatar,
  Button,
  TextField,
  Link,
  Alert,
  MenuItem,
  FormControlLabel,
  Radio,
  RadioGroup,
  FormLabel,
  FormControl,
  CircularProgress,
} from "@mui/material";
import PersonAddAltIcon from "@mui/icons-material/PersonAddAlt";
import { useNavigate, Link as RouterLink } from "react-router-dom";
import { registerAluno, registerProfessor } from "../services/authService";
import { UserRole } from "../types";

interface RegisterFormState {
  nome: string;
  email: string;
  senha: string;
  confirmarSenha: string;
  turma: string;
  perfil: UserRole;
}

const initialState: RegisterFormState = {
  nome: "",
  email: "",
  senha: "",
  confirmarSenha: "",
  turma: "",
  perfil: "aluno",
};

export default function Register() {
  const [form, setForm] = useState<RegisterFormState>(initialState);
  const [error, setError] = useState<string | null>(null);
  const [success, setSuccess] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleChange = (
    e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>
  ) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handlePerfilChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setForm({ ...form, perfil: e.target.value as UserRole, turma: "" });
  };

  const validate = () => {
    if (!form.nome || !form.email || !form.senha || !form.confirmarSenha) {
      setError("Preencha todos os campos obrigatórios.");
      return false;
    }
    if (form.perfil === "aluno" && !form.turma) {
      setError("Informe a turma.");
      return false;
    }
    if (form.senha.length < 6) {
      setError("A senha deve ter pelo menos 6 caracteres.");
      return false;
    }
    if (form.senha !== form.confirmarSenha) {
      setError("As senhas não conferem.");
      return false;
    }
    return true;
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    if (!validate()) return;
    setLoading(true);
    try {
      if (form.perfil === "aluno") {
        await registerAluno({
          nome: form.nome,
          email: form.email,
          senha: form.senha,
          turma: form.turma,
        });
      } else {
        await registerProfessor({
          nome: form.nome,
          email: form.email,
          senha: form.senha,
        });
      }
      setSuccess("Cadastro realizado com sucesso! Faça login.");
      setTimeout(() => navigate("/login"), 1800);
    } catch (err: any) {
      setError(
        err?.response?.data?.erro ||
          err?.response?.data?.msg ||
          "Erro ao cadastrar usuário. Tente novamente."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <Grid container component="main" sx={{ height: "100vh" }}>
      {/* Branding/informação lateral */}
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
            Faça parte da comunidade SIAS! Professores e alunos colaborando para uma educação melhor.
          </Typography>
        </Box>
      </Grid>

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
            maxWidth: 380,
          }}
        >
          <Avatar sx={{ m: 1, bgcolor: "primary.main" }}>
            <PersonAddAltIcon />
          </Avatar>
          <Typography component="h1" variant="h5">
            Cadastro
          </Typography>
          <Box
            component="form"
            sx={{ mt: 1, width: "100%" }}
            onSubmit={handleSubmit}
            autoComplete="off"
          >
            <FormControl component="fieldset" sx={{ mb: 2 }}>
              <FormLabel component="legend">Perfil</FormLabel>
              <RadioGroup
                row
                name="perfil"
                value={form.perfil}
                onChange={handlePerfilChange}
              >
                <FormControlLabel
                  value="aluno"
                  control={<Radio />}
                  label="Aluno"
                />
                <FormControlLabel
                  value="professor"
                  control={<Radio />}
                  label="Professor"
                />
              </RadioGroup>
            </FormControl>
            <TextField
              margin="normal"
              required
              fullWidth
              label="Nome completo"
              name="nome"
              value={form.nome}
              onChange={handleChange}
            />
            <TextField
              margin="normal"
              required
              fullWidth
              label="E-mail"
              name="email"
              type="email"
              value={form.email}
              onChange={handleChange}
            />
            {form.perfil === "aluno" && (
              <TextField
                margin="normal"
                required
                fullWidth
                label="Turma"
                name="turma"
                value={form.turma}
                onChange={handleChange}
              />
            )}
            <TextField
              margin="normal"
              required
              fullWidth
              label="Senha"
              name="senha"
              type="password"
              value={form.senha}
              onChange={handleChange}
              inputProps={{ minLength: 6 }}
              helperText="Mínimo 6 caracteres"
            />
            <TextField
              margin="normal"
              required
              fullWidth
              label="Confirmar senha"
              name="confirmarSenha"
              type="password"
              value={form.confirmarSenha}
              onChange={handleChange}
            />
            {error && (
              <Alert severity="error" sx={{ mt: 2 }}>
                {error}
              </Alert>
            )}
            {success && (
              <Alert severity="success" sx={{ mt: 2 }}>
                {success}
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
              {loading ? (
                <CircularProgress size={24} color="inherit" />
              ) : (
                "Cadastrar"
              )}
            </Button>
            <Grid container justifyContent="center">
              <Grid item>
                <Typography variant="body2">
                  Já tem conta?{" "}
                  <Link component={RouterLink} to="/login">
                    Faça login
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