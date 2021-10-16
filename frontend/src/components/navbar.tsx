import React from "react";
import {
  AppBar,
  Toolbar,
  CssBaseline,
  Typography,
  makeStyles,
  Theme,
  createStyles,
} from "@material-ui/core";
import { Link } from "react-router-dom";

const useStyles = makeStyles((theme: Theme) =>
  createStyles({
    bar: {
      backgroundColor: "#020917",
    },
    navlinks: {
      marginLeft: theme.spacing(10),
      display: "flex",
    },
    logo: {
      flexGrow: 1,
      cursor: "pointer",
      color: "#078af5",
    },
    link: {
      textDecoration: "none",
      color: "#078af5",
      fontSize: "20px",
      marginLeft: theme.spacing(20),
      "&:hover": {
        color: "#03f7ff",
        borderBottom: "1px solid white",
      },
    },
  })
);

export default function Navbar(): JSX.Element {
  const classes = useStyles();

  return (
    <AppBar position="static" className={classes.bar}>
      <CssBaseline />
      <Toolbar>
        <Typography variant="h4" className={classes.logo}>
          Find Your Pizza Friend!
        </Typography>
        <div className={classes.navlinks}>
          <Link to="/" className={classes.link}>
            Home
          </Link>
          <Link to="/pizza" className={classes.link}>
            Pizza
          </Link>
          <Link to="/contact" className={classes.link}>
            Contact
          </Link>
        </div>
      </Toolbar>
    </AppBar>
  );
}
