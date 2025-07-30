import React from "react";
import { Card, CardContent, CardActions, Typography, Box, IconButton, Tooltip } from "@mui/material";
import EventNoteIcon from "@mui/icons-material/EventNote";
import EditIcon from "@mui/icons-material/Edit";
import DeleteIcon from "@mui/icons-material/Delete";
import VisibilityIcon from "@mui/icons-material/Visibility";

export type Aula = {
  id: number;
  tema: string;
  data: string;
  grupo_aula_id: number;
};

type CardAulaProps = {
  aula: Aula;
  onEdit?: (aula: Aula) => void;
  onDelete?: (aula: Aula) => void;
  onView?: (aula: Aula) => void;
};

const CardAula: React.FC<CardAulaProps> = ({ aula, onEdit, onDelete, onView }) => (
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
        <EventNoteIcon color="success" fontSize="large" />
        <Typography variant="h6" fontWeight={700}>
          {aula.tema}
        </Typography>
      </Box>
      <Typography variant="body2" color="text.secondary">
        Data: {new Date(aula.data).toLocaleDateString()}
      </Typography>
    </CardContent>
    <CardActions>
      <Tooltip title="Ver detalhes">
        <IconButton onClick={() => onView && onView(aula)}>
          <VisibilityIcon />
        </IconButton>
      </Tooltip>
      <Tooltip title="Editar">
        <IconButton color="secondary" onClick={() => onEdit && onEdit(aula)}>
          <EditIcon />
        </IconButton>
      </Tooltip>
      <Tooltip title="Excluir">
        <IconButton color="error" onClick={() => onDelete && onDelete(aula)}>
          <DeleteIcon />
        </IconButton>
      </Tooltip>
    </CardActions>
  </Card>
);

export default CardAula;