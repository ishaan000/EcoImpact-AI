"use client";

import { useTheme } from "@mui/material/styles";
import { Box, Paper, Typography } from "@mui/material";
import ChatWindow from "../components/ChatWindow";
import ChatInput from "../components/ChatInput";
import ResetChatButton from "../components/ResetChatButton";
import ResetChatDialog from "../components/ResetChatDialog";
import SnackbarAlert from "../components/SnackbarAlert";
import { useChat } from "@/hooks/useChat";
import { useState } from "react";

export default function ChatPage() {
  const theme = useTheme();
  const { messages, sendMessage, resetChat, loading, messagesEndRef } =
    useChat();
  const [resetMessage, setResetMessage] = useState<string | null>(null);
  const [confirmOpen, setConfirmOpen] = useState(false);

  const handleResetChat = async () => {
    setConfirmOpen(false);
    try {
      const response = await resetChat();
      setResetMessage(response);
    } catch (error) {
      setResetMessage("Failed to reset memory. Try again.");
    }
  };

  return (
    <Box
      sx={{
        display: "flex",
        flexDirection: "column",
        height: "100vh",
        justifyContent: "center",
        alignItems: "center",
        bgcolor: theme.palette.background.default,
        p: 2,
      }}
    >
      <Paper
        sx={{
          width: "90%",
          maxWidth: 600,
          p: 2,
          borderRadius: 3,
          boxShadow: 3,
          bgcolor: theme.palette.background.paper,
          position: "relative",
        }}
      >
        <Box sx={{ position: "absolute", top: 10, right: 10 }}>
          <ResetChatButton onClick={() => setConfirmOpen(true)} />
        </Box>

        <Typography variant="h5" textAlign="center" gutterBottom>
          EcoImpact Agentic AI
        </Typography>

        <ChatWindow
          messages={messages}
          messagesEndRef={messagesEndRef as React.RefObject<HTMLDivElement>}
        />

        <ChatInput onSendMessage={sendMessage} loading={loading} />

        <ResetChatDialog
          open={confirmOpen}
          onClose={() => setConfirmOpen(false)}
          onConfirm={handleResetChat}
        />

        <SnackbarAlert
          message={resetMessage}
          onClose={() => setResetMessage(null)}
        />
      </Paper>
    </Box>
  );
}
