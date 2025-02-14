import { Snackbar, Alert } from "@mui/material";

interface SnackbarAlertProps {
  message: string | null;
  onClose: () => void;
}

const SnackbarAlert = ({ message, onClose }: SnackbarAlertProps) => {
  return (
    <Snackbar open={!!message} autoHideDuration={3000} onClose={onClose}>
      <Alert onClose={onClose} severity="info">
        {message}
      </Alert>
    </Snackbar>
  );
};

export default SnackbarAlert;
