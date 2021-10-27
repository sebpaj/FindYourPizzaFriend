import React from "react";
import { makeStyles } from "@mui/styles";
import { withStyles } from "@mui/styles";
import Accordion from "@mui/material/Accordion";
import AccordionSummary from "@mui/material/AccordionSummary";
import AccordionDetails from "@mui/material/AccordionDetails";
import Typography from "@mui/material/Typography";
import ExpandMoreIcon from "@mui/icons-material/ExpandMore";
import UserPizzas from "./user-pizzas";

const useStyles = makeStyles({
  root: {
    textAlign: "center",
    backgroundColor: "#00001a",
    color: "#078af5",
  },
  typography: {
    color: "#078af5",
    textAlign: "left",
    margin: "100",
  },
  table: {
    width: "100%",
    border: "2px solid #363b4a",
    backgroundColor: "#00001a",
    color: "#078af5",
  },
});

const StyledAccordionSummary = withStyles({
  root: {
    minHeight: 50,
    maxHeight: 500,
    backgroundColor: "#00001a",
    color: "#078af5",
    "&.Mui-expanded": {
      minHeight: 50,
      maxHeight: 500,
      backgroundColor: "black",
      color: "#078af5",
    },
  },
  expandIcon: {
    order: -1,
  },
})(AccordionSummary);

export default function UserPizzasAccordion(): JSX.Element {
  const classes = useStyles();
  return (
    <div>
      <Accordion sx={{ backgroundColor: "#00001a", width: "800px" }}>
        <StyledAccordionSummary
          expandIcon={<ExpandMoreIcon />}
          aria-controls="panel1a-content"
          id="panel1a-header"
        >
          <Typography
            variant="h6"
            gutterBottom
            component="div"
            sx={{ pl: 1 }}
            className={classes.typography}
          >
            Your Pizzas
          </Typography>
        </StyledAccordionSummary>
        <AccordionDetails sx={{ backgroundColor: "black" }}>
          <UserPizzas />
        </AccordionDetails>
      </Accordion>
    </div>
  );
}
