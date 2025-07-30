import React from "react";
import { Card, CardContent, CardActions, Typography, Box, IconButton, Tooltip } from "@mui/material";
import MenuBookIcon from "@mui/icons-material/MenuBook";
import EditIcon from "@mui/icons-material/Edit";
import DeleteIcon from "@mui/icons-material/Delete";
import VisibilityIcon from "@mui/icons-material/Visibility";
import GetAppIcon from "@mui/icons-material/GetApp";

export type Material = {
  id: number;
  titulo: string;
  tipo: string;
  data_publicacao: string;
  autor_id: number;
  arquivo_url?: string;
};

type CardMaterialProps = {
  material: Material;
  onEdit?: (material: Material) => void;
  onDelete?: (material: Material) => void;
  onView?: (material: Material) => void;
  onDownload?: (material: Material) => void;
};

const CardMaterial: React.FC<CardMaterialProps> = ({
  material,
  onEdit,
  onDelete,
  onView,
  onDownload
}) => (
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
        <MenuBookIcon color="secondary" fontSize="large" />
        <Typography variant="h6" fontWeight={700}>
          {material.titulo}
        </Typography>
      </Box>
      <Typography variant="body2" color="text.secondary">
        Tipo: {material.tipo}
      </Typography>
      <Typography variant="body2" color="text.secondary">
        Publicado em: {new Date(material.data_publicacao).toLocaleDateString()}
      </Typography>
    </CardContent>
    <CardActions>
      <Tooltip title="Ver detalhes">
        <IconButton onClick={() => onView && onView(material)}>
          <VisibilityIcon />
        </IconButton>
      </Tooltip>
      <Tooltip title="Editar">
        <IconButton color="secondary" onClick={() => onEdit && onEdit(material)}>
          <EditIcon />
        </IconButton>
      </Tooltip>
      <Tooltip title="Excluir">
        <IconButton color="error" onClick={() => onDelete && onDelete(material)}>
          <DeleteIcon />
        </IconButton>
      </Tooltip>
      {material.arquivo_url && (
        <Tooltip title="Baixar">
          <IconButton
            onClick={() =>
              onDownload
                ? onDownload(material)
                : window.open(material.arquivo_url, "_blank")
            }
          >
            <GetAppIcon />
          </IconButton>
        </Tooltip>
      )}
    </CardActions>
  </Card>
);

export default CardMaterial;