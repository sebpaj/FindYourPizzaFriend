import React, { useState } from "react";
import { makeStyles } from "@mui/styles";
import Box from "@mui/material/Box";
import Container from "@mui/material/Container";

import Login from "./log-in";
import Logout from "./log-out";

import WelcomeScreen from "./welcome-screen";
import CreatePizza from "./create-pizza";
import UserPizzas from "./user-pizzas";

const useStyles = makeStyles({
  root: {
    textAlign: "center",
  },
});

export default function MainLayout(): JSX.Element {
  const [isLoggedIn, setIsLoggedIn] = useState<boolean>(false);
  const [token, setToken] = useState<string | null>(null);
  const [name, setName] = useState<string | null>(null);
  const [email, setEmail] = useState<string | null>(null);
  const [imageUrl, setImageUrl] = useState<string | undefined>("");
  console.log("is logged in", isLoggedIn);
  const classes = useStyles();

  return (
    <React.Fragment>
      <Container className={classes.root} maxWidth="xl">
        <WelcomeScreen
          isLoggedIn={isLoggedIn}
          name={name}
          imageUrl={imageUrl}
        />
        <Box>
          {!isLoggedIn ? (
            <Login
              setIsLoggedIn={setIsLoggedIn}
              setToken={setToken}
              setName={setName}
              setEmail={setEmail}
              setImageUrl={setImageUrl}
            />
          ) : (
            <React.Fragment>
              <Logout
                setIsLoggedIn={setIsLoggedIn}
                setToken={setToken}
                setName={setName}
                setEmail={setEmail}
                setImageUrl={setImageUrl}
              />
              ,
              <CreatePizza />,
              <UserPizzas />
            </React.Fragment>
          )}
        </Box>
      </Container>
    </React.Fragment>
  );
}
