export type UserRole = "aluno" | "professor";

export interface LoginPayload {
  email: string;
  senha: string;
}

export interface LoginResponse {
  access_token: string;
  nome: string;
  role: UserRole;
  id: number;
}

export interface RegisterAlunoPayload {
  nome: string;
  email: string;
  senha: string;
  turma: string;
}
export interface RegisterProfessorPayload {
  nome: string;
  email: string;
  senha: string;
}