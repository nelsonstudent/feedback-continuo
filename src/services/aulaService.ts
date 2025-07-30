import axios from "axios";
import { Aula } from "../components/CardAula";

const API_URL = process.env.REACT_APP_API_URL || "http://localhost:5000";

export const buscarAulas = async (): Promise<Aula[]> => {
  const response = await axios.get<Aula[]>(`${API_URL}/aulas/`);
  return response.data;
};

export const criarAula = async (data: Omit<Aula, "id">) => {
  const response = await axios.post(`${API_URL}/aulas/`, data);
  return response.data;
};