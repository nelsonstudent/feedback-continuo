import React from "react";
import { Card, CardContent, CardActions, Typography, Box, IconButton, Tooltip } from "@mui/material";
import SchoolIcon from "@mui/icons-material/School";
import EditIcon from "@mui/icons-material/Edit";
import DeleteIcon from "@mui/icons-material/Delete";
import VisibilityIcon from "@mui/icons-material/Visibility";

export type Turma = {
  id: number;
  codigo_turma: string;
  mentor: { id: number; nome: string };
};

type CardTurmaProps = {
  turma: Turma;
  onEdit?: (turma: Turma) => void;
  onDelete?: (turma: Turma) => void;
  onView?: (turma: Turma) => void;
};

const CardTurma: React.FC<CardTurmaProps> = ({ turma, onEdit, onDelete, onView }) => (
  <Card
    elevation={6}
    sx={{
      minWidth: 280,
      borderRadius: 3,
      boxShadow: 3,
      mb: 2,
      transition: "box-shadow 0.2s",
      "&:hover": { boxShadow: 8 }
    }}
  >
    <CardContent>
      <Box display="flex" alignItems="center" gap={1} mb={1}>
        <SchoolIcon color="primary" fontSize="large" />
        <Typography variant="h6" fontWeight={700}>
          {turma.codigo_turma}
        </Typography>
      </Box>
      <Typography variant="body2" color="text.secondary">
        Mentor: {turma.mentor?.nome}
      </Typography>
    </CardContent>
    <CardActions>
      <Tooltip title="Ver detalhes">
        <IconButton onClick={() => onView && onView(turma)}>
          <VisibilityIcon />
        </IconButton>
      </Tooltip>
      <Tooltip title="Editar">
        <IconButton color="secondary" onClick={() => onEdit && onEdit(turma)}>
          <EditIcon />
        </IconButton>
      </Tooltip>
      <Tooltip title="Excluir">
        <IconButton color="error" onClick={() => onDelete && onDelete(turma)}>
          <DeleteIcon />
        </IconButton>
      </Tooltip>
    </CardActions>
  </Card>
);

export default CardTurma;