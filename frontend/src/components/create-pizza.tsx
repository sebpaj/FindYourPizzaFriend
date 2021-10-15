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
      <Button variant="contained">Create Pizza</Button>
      <Button variant="contained">Find Your Pizza Friends!:)</Button>
    </Stack>
  );
}
