import { Query } from "react-apollo";

import gql from "graphql-tag";
import React from "react";

const PostListView = () => (
  <Query
    query={gql`
      {
        yay
      }
    `}
  >
    {({ loading, error, data }) => {
      if (loading) return <p>Loading...</p>;
      if (error) return <p>Error :(</p>;

      return (
        <div>
          <h1>Hey yo</h1>
          <ul>{data.yay}</ul>
        </div>
      );
    }}
  </Query>
);

export default PostListView;
