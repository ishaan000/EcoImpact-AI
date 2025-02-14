import {
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  Button,
} from "@mui/material";

interface ResetChatDialogProps {
  open: boolean;
  onClose: () => void;
  onConfirm: () => void;
}

const ResetChatDialog = ({
  open,
  onClose,
  onConfirm,
}: ResetChatDialogProps) => {
  return (
    <Dialog open={open} onClose={onClose}>
      <DialogTitle>Reset Chat?</DialogTitle>
      <DialogContent>
        Are you sure you want to reset the chat? This will erase all chat
        history.
      </DialogContent>
      <DialogActions>
        <Button onClick={onClose}>Cancel</Button>
        <Button onClick={onConfirm} color="error">
          Reset
        </Button>
      </DialogActions>
    </Dialog>
  );
};

export default ResetChatDialog;
