import axios from "axios";
import { Turma } from "../components/CardTurma";

const API_URL = process.env.REACT_APP_API_URL || "http://localhost:5000";

export const buscarTurmas = async (): Promise<Turma[]> => {
  const response = await axios.get<Turma[]>(`${API_URL}/grupo_aula/`);
  return response.data;
};

export const criarTurma = async (data: Omit<Turma, "id">) => {
  const response = await axios.post(`${API_URL}/grupo_aula/`, data);
  return response.data;
};