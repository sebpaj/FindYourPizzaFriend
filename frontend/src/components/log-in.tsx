import React from "react";
import GoogleLogin, {
  GoogleLoginResponse,
  GoogleLoginResponseOffline,
} from "react-google-login";

export interface LoginProps {
  setIsLoggedIn: React.Dispatch<React.SetStateAction<boolean>>;
  setToken: React.Dispatch<React.SetStateAction<string | null>>;
  setName: React.Dispatch<React.SetStateAction<string | null>>;
  setEmail: React.Dispatch<React.SetStateAction<string | null>>;
  setImageUrl: React.Dispatch<React.SetStateAction<string | undefined>>;
}

const clientId: string = process.env.REACT_APP_GOOGLE_CLIENT_ID ?? "";

export default function Login(props: LoginProps): JSX.Element {
  const { setIsLoggedIn, setToken, setName, setEmail, setImageUrl } = props;
  const onSuccess = (res: any) => {
    console.log("res below");
    console.log(res);
    setIsLoggedIn(true);
    setToken(res.tokenId);
    setName(res.profileObj.name);
    setEmail(res.profileObj.email);
    setImageUrl(res.profileObj.imageUrl);
  };

  const onFailure = (res: GoogleLoginResponse | GoogleLoginResponseOffline) => {
    console.log("[Login Failed] for", res);
  };

  return (
    <div>
      <GoogleLogin
        clientId={clientId}
        buttonText="Login"
        onSuccess={onSuccess}
        onFailure={onFailure}
        cookiePolicy={"single_host_origin"}
        style={{ marginTop: "100px" }}
        isSignedIn={true}
      ></GoogleLogin>
    </div>
  );
}
