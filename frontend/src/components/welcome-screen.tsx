import React from "react";
import { makeStyles } from "@mui/styles";
import Box from "@mui/material/Box";
import Paper from "@mui/material/Paper";
import Grid from "@mui/material/Grid";

export interface WelcomeScreenProps {
  isLoggedIn: boolean;
  name: string | null;
  imageUrl: string | undefined;
}

const useStyles = makeStyles({
  root: {
    textAlign: "center",
    padding: "10px 50px",
  },
  item: {
    color: "#078af5",
    padding: "10px",
  },
});

export default function WelcomeScreen(props: WelcomeScreenProps): JSX.Element {
  const { isLoggedIn, name, imageUrl } = props;
  console.log("welcome screen", isLoggedIn);

  const classes = useStyles();

  if (isLoggedIn) {
    return (
      <Box sx={{ flexGrow: 1 }}>
        <Grid
          container
          spacing={0}
          direction="column"
          alignItems="center"
          justifyContent="center"
          className={classes.root}
        >
          <Grid item xs={2} className={classes.item}>
            Welcome {name}
          </Grid>
          <Grid item xs={2} className={classes.item}>
            <img src={imageUrl} alt="new" />
          </Grid>
        </Grid>
      </Box>
    );
  }
  return (
    <Box sx={{ flexGrow: 1 }}>
      <Grid
        container
        spacing={0}
        direction="column"
        alignItems="center"
        justifyContent="center"
        className={classes.root}
      >
        <Grid item xs={2} className={classes.item}>
          Welcome stranger. Please log in.
        </Grid>
      </Grid>
    </Box>
  );
}
