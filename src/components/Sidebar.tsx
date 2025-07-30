import React from "react";
import { Drawer, Box, Avatar, Typography, Divider, List, ListItem, ListItemIcon, ListItemText } from "@mui/material";
import SchoolIcon from "@mui/icons-material/School";
import DescriptionIcon from "@mui/icons-material/Description";
import ExitToAppIcon from "@mui/icons-material/ExitToApp";

type SidebarProps = {
  nome: string;
  email?: string;
  fotoUrl?: string;
  onLogout?: () => void;
};

const Sidebar: React.FC<SidebarProps> = ({ nome, email, fotoUrl, onLogout }) => (
  <Drawer
    variant="permanent"
    anchor="left"
    sx={{
      width: 240,
      flexShrink: 0,
      [`& .MuiDrawer-paper`]: { width: 240, boxSizing: "border-box" }
    }}
  >
    <Box sx={{ p: 3, display: "flex", flexDirection: "column", alignItems: "center" }}>
      <Avatar src={fotoUrl} sx={{ width: 80, height: 80, mb: 2 }}>
        {!fotoUrl && nome ? nome[0] : ""}
      </Avatar>
      <Typography variant="h6">{nome}</Typography>
      {email && (
        <Typography variant="body2" color="textSecondary">{email}</Typography>
      )}
    </Box>
    <Divider />
    <List>
      <ListItem button>
        <ListItemIcon><SchoolIcon /></ListItemIcon>
        <ListItemText primary="Turmas" />
      </ListItem>
      <ListItem button>
        <ListItemIcon><DescriptionIcon /></ListItemIcon>
        <ListItemText primary="Materiais" />
      </ListItem>
      <ListItem button onClick={onLogout}>
        <ListItemIcon><ExitToAppIcon /></ListItemIcon>
        <ListItemText primary="Sair" />
      </ListItem>
    </List>
  </Drawer>
);

export default Sidebar;