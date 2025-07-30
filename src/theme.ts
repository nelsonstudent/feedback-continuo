import { createTheme } from '@mui/material/styles';

const theme = createTheme({
  palette: {
    primary: { main: '#3B82F6' },    // Azul Elétrico Suave
    secondary: { main: '#7C3AED' },  // Roxo Educacional
    success: { main: '#10B981' },    // Verde Sucesso
    error: { main: '#EF4444' },      // Vermelho Alert
    background: { default: '#F9FAFB' },
    text: {
      primary: '#1F2937',            // Cinza Grafite
      secondary: '#6B7280',          // Cinza Neutro
    },
  },
  typography: {
    fontFamily: [
      'Inter',
      'Poppins',
      'ui-sans-serif',
      'system-ui',
      'sans-serif',
    ].join(','),
    h1: { fontWeight: 700 },
    h2: { fontWeight: 700 },
    h3: { fontWeight: 700 },
    button: { textTransform: 'none', fontWeight: 700 }
  },
  shape: {
    borderRadius: 8, // Bordas arredondadas suaves
  },
});

export default theme;