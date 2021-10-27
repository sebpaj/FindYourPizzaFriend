import React from "react";
import { styled } from "@mui/material/styles";
import { makeStyles } from "@mui/styles";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell, { tableCellClasses } from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";

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
    border: "2px solid #363b4a",
    backgroundColor: "#00001a",
    color: "#078af5",
  },
});

const StyledTableCell = styled(TableCell)(({ theme }) => ({
  [`&.${tableCellClasses.head}`]: {
    fontSize: 14,
    backgroundColor: theme.palette.common.black,
    color: "#078af5",
  },
  [`&.${tableCellClasses.body}`]: {
    fontSize: 14,
    backgroundColor: theme.palette.common.black,
    color: "#078af5",
  },
}));

export default function UserPizzas(): JSX.Element {
  const classes = useStyles();
  const rows: string[][] = [
    ["Capriociosa", "[cheese, ham, mushrooms]"],
    ["Salame", "[salami, cheese, mushrooms]"],
  ];
  return (
    <React.Fragment>
      <TableContainer component={Paper} className={classes.table}>
        <Table sx={{ minWidth: 350 }} size="small" aria-label="a dense table">
          <TableHead>
            <TableRow>
              <StyledTableCell>Pizza</StyledTableCell>
              <StyledTableCell align="center">Ingredients</StyledTableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {rows.map((row) => (
              <TableRow
                key={row[0]}
                sx={{ "&:last-child td, &:last-child th": { border: 0 } }}
              >
                <StyledTableCell component="th" scope="row">
                  {row[0]}
                </StyledTableCell>
                <StyledTableCell align="center">{row[1]}</StyledTableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </React.Fragment>
  );
}
