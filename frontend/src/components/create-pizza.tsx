import React from "react";
import { makeStyles } from "@mui/styles";
import Button from "@mui/material/Button";
import Stack from "@mui/material/Stack";

const useStyles = makeStyles({
  root: {
    padding: "25px 5px",
  },
});

export default function CreatePizza(): JSX.Element {
  const classes = useStyles();
  return (
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
          backgroundColor: "#0f1d45",
          color: "#078af5",
          padding: "3px 18px",
          fontSize: "18px",
        }}
        onClick={() => console.log("clicked create button")}
      >
        Create Pizza
      </Button>
      <Button
        variant="contained"
        style={{
          border: "2px solid #363b4a",
          backgroundColor: "#0f1d45",
          color: "#078af5",
          padding: "3px 18px",
          fontSize: "18px",
        }}
        onClick={() => console.log("clicked find button")}
      >
        Find Your Pizza Friends!:)
      </Button>
    </Stack>
  );
}
