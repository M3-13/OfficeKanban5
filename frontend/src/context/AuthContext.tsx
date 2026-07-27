import { createContext, useContext, type ReactNode } from "react";
import type { AuthContextType, LoginCredentials, RegisterCredentials, User } from "../types";

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export function AuthProvider({ children }: { children: ReactNode }) {
  const user: User | null = null;
  const token: string | null = null;
  const isAuthenticated = false;

  const login = async (_credentials: LoginCredentials): Promise<void> => {};
  const register = async (_credentials: RegisterCredentials): Promise<void> => {};
  const logout = (): void => {};

  return (
    <AuthContext.Provider value={{ user, token, isAuthenticated, login, register, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth(): AuthContextType {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error("useAuth must be used within an AuthProvider");
  }
  return context;
}
