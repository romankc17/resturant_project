import React from "react";
import Body from "./Body";
import Header from "./Header";
import "../CSS/Home.css";

function Home() {
  return (
    <div className="home">
      <Header />
      <Body
        image="https://s3-media0.fl.yelpcdn.com/bphoto/4quugw5FJrEENowfhzQxEg/ls.jpg"
        location="BankRoad,Bhairahawa"
        rating={4}
        name="Pizza Hut"
      />

      <Body
        image="https://www.qsrmagazine.com/sites/default/files/styles/story_page/public/story/mcdonalds-getting-even-more-serious-about-tech.jpg?itok=QNbr6UbC"
        location="Lakhanchowak,Bhairahawa"
        rating={5}
        name="McDonald's"
      />
    </div>
  );
}

export default Home;
