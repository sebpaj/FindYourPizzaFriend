import React from "react";
import { makeStyles } from "@mui/styles";
import Box from "@mui/material/Box";
import Container from "@mui/material/Container";

const useStyles = makeStyles({
  root: {
    textAlign: "center",
    color: "lightblue",
  },
});

export default function MainLayout(): JSX.Element {
  const classes = useStyles();
  return (
    <React.Fragment>
      <Container className={classes.root} maxWidth="xl">
        <Box>This is me</Box>
      </Container>
    </React.Fragment>
  );
}
