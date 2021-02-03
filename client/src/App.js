import logo from './logo.svg';
import './App.css';
import { gql, useQuery } from '@apollo/client';
import { ApolloProvider, ApolloClient, InMemoryCache } from '@apollo/client';


const GET_QUERY = gql` 
    { yay }
`;

const client = new ApolloClient({
    uri:
    process.env.NODE_ENV === "production"
    ? "/gql"
    : "http://localhost:5000/graphql/",
    cache: new InMemoryCache()
});

function Sample() {
  const { loading, error, data } = useQuery(GET_QUERY);

  if (loading) return 'Loading...';
  if (error) return `Error! ${error.message}`;

  return (
      <div>{data.yay}</div>
  );
}

function App() {
  return (
  <ApolloProvider client={client}>
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          <Sample/>
        </a>
      </header>
    </div>
 </ApolloProvider>
  );
}

export default App;
