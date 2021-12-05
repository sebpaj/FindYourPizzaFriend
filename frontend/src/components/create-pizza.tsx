import React, { useState } from "react";
import { makeStyles } from "@mui/styles";
import Button from "@mui/material/Button";
import Box from "@mui/material/Box";
import Modal from "@mui/material/Modal";
import Stack from "@mui/material/Stack";
import Typography from "@mui/material/Typography";

import { useQuery, gql } from "@apollo/client";

const CATEGORIES_WITH_INGREDIENTS_QUERY = gql`
  query ALL_CATEGORIES {
    allCategories {
      edges {
        node {
          name
          ingredients {
            edges {
              node {
                name
              }
            }
          }
        }
      }
    }
  }
`;

const useStyles = makeStyles({
  root: {
    padding: "25px 5px",
  },
});

interface CategoryWithIngredients {
  name: string;
  ingredients: string[];
}

export default function CreatePizza(): JSX.Element {
  const [isPizzaModalOpen, setIsPizzaModalOpen] = useState<boolean>(false);
  const handleIsPizzaModelOpen = () => setIsPizzaModalOpen(!isPizzaModalOpen);
  const classes = useStyles();
  const { data, loading, error } = useQuery(CATEGORIES_WITH_INGREDIENTS_QUERY);

  if (loading) return <div>Loading...</div>;
  if (error) return <pre>{error.message}</pre>;

  const categories: CategoryWithIngredients[] = data.allCategories.edges.map(
    (edge: any) => ({
      name: edge.node.name,
      ingredients: edge.node.ingredients.edges.map(
        (edge: any) => edge.node.name
      ),
    })
  );

  // TODO Pass categories as props to create-pizza-table and use pizza-cateogry table later for every category

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
