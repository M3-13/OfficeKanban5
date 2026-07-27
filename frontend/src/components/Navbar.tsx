import { useAuth } from "../context/AuthContext";

export default function Navbar() {
  void useAuth();
  return <header></header>;
}
