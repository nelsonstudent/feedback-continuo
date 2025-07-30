import axios from "axios";
import { LoginPayload, LoginResponse, RegisterAlunoPayload, RegisterProfessorPayload } from "../types";

const API_URL = process.env.REACT_APP_API_URL || "http://localhost:5000";

export async function login(payload: LoginPayload): Promise<LoginResponse> {
  const response = await axios.post(`${API_URL}/login`, payload);
  return response.data;
}

export async function registerAluno(payload: RegisterAlunoPayload) {
  const response = await axios.post(`${API_URL}/alunos/`, payload);
  return response.data;
}

export async function registerProfessor(payload: RegisterProfessorPayload) {
  const response = await axios.post(`${API_URL}/professores/`, payload);
  return response.data;
}