import React from "react";

export interface WelcomeScreenProps {
  isLoggedIn: boolean;
  name: string | null;
  imageUrl: string | undefined;
}

export default function WelcomeScreen(props: WelcomeScreenProps): JSX.Element {
  const { isLoggedIn, name, imageUrl } = props;

  console.log("welcome screen", isLoggedIn);

  if (isLoggedIn) {
    return (
      <div>
        <img src={imageUrl} alt="new" />
        <p>Welcome {name}</p>
      </div>
    );
  }
  return <p>Welcome stranger. Please log in.</p>;
}
