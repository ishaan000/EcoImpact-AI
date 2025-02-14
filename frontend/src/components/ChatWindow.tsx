import { Box, Paper, Typography } from "@mui/material";
import { useTheme } from "@mui/material/styles";

type Message = { text: string; sender: "user" | "bot" };

interface ChatWindowProps {
  messages: Message[];
  messagesEndRef: React.RefObject<HTMLDivElement>;
}

const formatMessage = (text: string) => {
  return text
    .replace(/\n{2,}/g, "\n")
    .replace(/\d+\.\s/g, "\n• ")
    .replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>")
    .trim();
};

const ChatWindow = ({ messages, messagesEndRef }: ChatWindowProps) => {
  const theme = useTheme();

  return (
    <Box
      sx={{
        height: 400,
        overflowY: "auto",
        display: "flex",
        flexDirection: "column",
        gap: 2,
        p: 2,
        bgcolor: theme.palette.background.paper,
        borderRadius: 2,
        boxShadow: 1,
      }}
    >
      {messages.map((msg, index) => (
        <Paper
          key={index}
          sx={{
            p: 1.5,
            maxWidth: "80%",
            alignSelf: msg.sender === "user" ? "flex-end" : "flex-start",
            bgcolor:
              msg.sender === "user" ? theme.palette.primary.main : "#eeeeee",
            color: msg.sender === "user" ? "white" : "black",
            borderRadius: 2,
          }}
        >
          <Typography
            component="div"
            sx={{ whiteSpace: "pre-line" }}
            dangerouslySetInnerHTML={{ __html: formatMessage(msg.text) }}
          />
        </Paper>
      ))}
      <div ref={messagesEndRef} />
    </Box>
  );
};

export default ChatWindow;
