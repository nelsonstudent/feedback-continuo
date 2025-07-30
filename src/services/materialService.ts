import axios from "axios";
import { Material } from "../components/CardMaterial";

const API_URL = process.env.REACT_APP_API_URL || "http://localhost:5000";

export const buscarMateriais = async (): Promise<Material[]> => {
  const response = await axios.get<Material[]>(`${API_URL}/materiais/`);
  return response.data;
};

export const criarMaterial = async (formData: FormData) => {
  const response = await axios.post(`${API_URL}/materiais/`, formData, {
    headers: { "Content-Type": "multipart/form-data" },
  });
  return response.data;
};