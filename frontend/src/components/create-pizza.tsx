import React, { useState } from "react";
import { makeStyles } from "@mui/styles";
import Button from "@mui/material/Button";
import Box from "@mui/material/Box";
import Modal from "@mui/material/Modal";
import Stack from "@mui/material/Stack";
import Typography from "@mui/material/Typography";

const useStyles = makeStyles({
  root: {
    padding: "25px 5px",
  },
});

export default function CreatePizza(): JSX.Element {
  const [isPizzaModalOpen, setIsPizzaModalOpen] = useState<boolean>(false);
  const handleIsPizzaModelOpen = () => setIsPizzaModalOpen(!isPizzaModalOpen);
  const classes = useStyles();

  return (
    <React.Fragment>
      <Stack
        className={classes.root}
        spacing={2}
        direction="row"
        alignItems="center"
        justifyContent="center"
      >
        <Button
          variant="contained"
          style={{
            border: "2px solid #363b4a",
            backgroundColor: "#00001a",
            color: "#078af5",
            padding: "3px 18px",
            fontSize: "18px",
          }}
          onClick={() => handleIsPizzaModelOpen()}
        >
          Create Pizza
        </Button>
        <Button
          variant="contained"
          style={{
            border: "2px solid #363b4a",
            backgroundColor: "#00001a",
            color: "#078af5",
            padding: "3px 18px",
            fontSize: "18px",
          }}
          onClick={() => console.log("clicked find button")}
        >
          Find Your Pizza Friends!:)
        </Button>
      </Stack>
      <Modal
        open={isPizzaModalOpen}
        onClose={handleIsPizzaModelOpen}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
      >
        <Box
          sx={{
            position: "absolute",
            top: "30%",
            left: "50%",
            transform: "translate(-50%, -50%)",
            width: 800,
            backgroundColor: "#00001a",
            color: "#078af5",
            border: "2px solid #363b4a",
            boxShadow: 24,
            p: 4,
          }}
        >
          <Typography id="modal-modal-title" variant="h6" component="h2">
            Text in a modal
          </Typography>
          <Typography id="modal-modal-description" sx={{ mt: 2 }}>
            Duis mollis, est non commodo luctus, nisi erat porttitor ligula.
          </Typography>
        </Box>
      </Modal>
    </React.Fragment>
  );
}
