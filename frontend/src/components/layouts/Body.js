import React from "react";

function Body({ image, name, location, rating }) {
  return (
    <div className="body">
      <img src={image} />
      <div className="body__info">
        <h4>{name}</h4>
        <span>{location}</span>
        <div className="product__rating">
          {Array(rating)
            .fill()
            .map((_) => (
              <p>⭐</p>
            ))}
        </div>
      </div>
    </div>
  );
}

export default Body;
