import React from "react";
import { makeStyles } from "@mui/styles";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";
import Typography from "@mui/material/Typography";

const useStyles = makeStyles({
  root: {
    textAlign: "center",
    backgroundColor: "#00001a",
    color: "#078af5",
  },
  typography: {
    color: "#078af5",
    textAlign: "left",
    margin: "100    ",
  },
  table: {
    width: "100%",
  },
});

export default function UserPizzas(): JSX.Element {
  const classes = useStyles();
  const rows: string[][] = [
    ["Capriociosa", "[cheese, ham, mushrooms]"],
    ["Salame", "[salami, cheese, mushrooms]"],
  ];
  return (
    <React.Fragment>
      <Typography
        variant="h6"
        gutterBottom
        component="div"
        sx={{ pl: 30 }}
        className={classes.typography}
      >
        Your Pizzas
      </Typography>

      <TableContainer
        component={Paper}
        sx={{ width: 700, position: "absolute", top: "50%", left: "23.5%" }}
      >
        <Table sx={{ minWidth: 350 }} size="small" aria-label="a dense table">
          <TableHead>
            <TableRow>
              <TableCell>Pizza</TableCell>
              <TableCell align="center">Ingredients</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {rows.map((row) => (
              <TableRow
                key={row[0]}
                sx={{ "&:last-child td, &:last-child th": { border: 0 } }}
              >
                <TableCell component="th" scope="row">
                  {row[0]}
                </TableCell>
                <TableCell align="center">{row[1]}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </React.Fragment>
  );
}
