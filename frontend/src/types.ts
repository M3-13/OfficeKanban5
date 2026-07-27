export interface User {
  id: number;
  email: string;
}

export interface LoginCredentials {
  email: string;
  password: string;
}

export interface RegisterCredentials {
  email: string;
  password: string;
}

export interface Board {
  id: number;
  title: string;
  user_id: number;
}

export interface Card {
  id: number;
  title: string;
  description: string | null;
  status: CardStatus;
  position: number;
  board_id: number;
}

export type CardStatus = "todo" | "in_progress" | "done";

export interface AuthContextType {
  user: User | null;
  token: string | null;
  isAuthenticated: boolean;
  login: (credentials: LoginCredentials) => Promise<void>;
  register: (credentials: RegisterCredentials) => Promise<void>;
  logout: () => void;
}
