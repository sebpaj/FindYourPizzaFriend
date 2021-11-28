import React from "react";
import GoogleLogin, {
  GoogleLoginResponse,
  GoogleLoginResponseOffline,
} from "react-google-login";
import { gql, useMutation } from "@apollo/client";

export interface LoginProps {
  setIsLoggedIn: React.Dispatch<React.SetStateAction<boolean>>;
  setToken: React.Dispatch<React.SetStateAction<string | null>>;
  setName: React.Dispatch<React.SetStateAction<string | null>>;
  setEmail: React.Dispatch<React.SetStateAction<string | null>>;
  setImageUrl: React.Dispatch<React.SetStateAction<string | undefined>>;
}

const clientId: string = process.env.REACT_APP_GOOGLE_CLIENT_ID ?? "";
const LOGIN_MUTATION = gql`
  mutation Login($input: LoginMutationInput!) {
    login(input: $input) {
      success
    }
  }
`;

export default function Login(props: LoginProps): JSX.Element {
  const { setIsLoggedIn, setToken, setName, setEmail, setImageUrl } = props;
  const [login, { data, loading, error }] = useMutation(LOGIN_MUTATION);
  const onSuccess = (res: any) => {
    setIsLoggedIn(true);
    setToken(res.tokenId);
    setName(res.profileObj.name);
    setEmail(res.profileObj.email);
    setImageUrl(res.profileObj.imageUrl);

    console.log("user logged, calling mutation");
    login({
      variables: {
        input: {
          firstName: res.profileObj.name,
          email: res.profileObj.email,
          imageUrl: res.profileObj.imageUrl,
        },
      },
    });
    console.log("data", data, "loading", loading, "error", error);
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
