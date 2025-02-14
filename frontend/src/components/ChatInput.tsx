import { TextField, Button, Box, CircularProgress } from "@mui/material";
import { useState } from "react";

interface ChatInputProps {
  onSendMessage: (message: string) => void;
  loading: boolean;
}

const ChatInput = ({ onSendMessage, loading }: ChatInputProps) => {
  const [userInput, setUserInput] = useState("");

  const handleSend = () => {
    if (!userInput.trim()) return;
    onSendMessage(userInput);
    setUserInput("");
  };

  const handleKeyDown = (event: React.KeyboardEvent<HTMLInputElement>) => {
    if (event.key === "Enter" && !event.shiftKey) {
      event.preventDefault();
      handleSend();
    }
  };

  return (
    <Box sx={{ display: "flex", gap: 1, mt: 2 }}>
      <TextField
        fullWidth
        variant="outlined"
        label="Ask about sustainability."
        value={userInput}
        onChange={(e) => setUserInput(e.target.value)}
        onKeyDown={handleKeyDown}
        disabled={loading}
      />
      <Button
        variant="contained"
        color="primary"
        onClick={handleSend}
        disabled={loading}
      >
        {loading ? <CircularProgress size={24} /> : "Send"}
      </Button>
    </Box>
  );
};

export default ChatInput;
