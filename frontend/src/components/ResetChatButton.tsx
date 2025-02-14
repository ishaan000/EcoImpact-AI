import { IconButton, Tooltip } from "@mui/material";
import RestartAltIcon from "@mui/icons-material/RestartAlt";

interface ResetChatButtonProps {
  onClick: () => void;
}

const ResetChatButton = ({ onClick }: ResetChatButtonProps) => {
  return (
    <Tooltip title="Reset Chat">
      <IconButton color="secondary" onClick={onClick}>
        <RestartAltIcon />
      </IconButton>
    </Tooltip>
  );
};

export default ResetChatButton;
