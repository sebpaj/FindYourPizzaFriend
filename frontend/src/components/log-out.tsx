import React from "react";
import { GoogleLogout } from "react-google-login";
import { LoginProps as LogutProps } from "./log-in";

const clientId: string = process.env.REACT_APP_GOOGLE_CLIENT_ID ?? "";

export default function Logout(props: LogutProps): JSX.Element {
  const { setIsLoggedIn, setToken, setName, setEmail, setImageUrl } = props;
  const onSuccess = () => {
    console.log("[Log out] succesfully");
    setIsLoggedIn(false);
    setToken(null);
    setName(null);
    setEmail(null);
    setImageUrl("");
  };

  return (
    <div>
      <GoogleLogout
        clientId={clientId}
        buttonText="Logout"
        onLogoutSuccess={onSuccess}
      ></GoogleLogout>
    </div>
  );
}
