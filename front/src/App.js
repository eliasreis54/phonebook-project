import React from 'react';
import { Container, InputLabel, FormControl, Input, Button } from '@material-ui/core';

import './App.css';

function App() {
  return (
    <div>
      <header className="App-header">
        <p>Phoonebook project</p>
      </header>
      <Container className="middle-layout">
        <Container className="form">
          <FormControl>
            <InputLabel htmlFor="name">Name</InputLabel>
            <Input id="name" aria-describedby="name" />
          </FormControl>
          <FormControl>
            <InputLabel htmlFor="email">Email address</InputLabel>
            <Input id="email" aria-describedby="email address" />
          </FormControl>
          <FormControl>
            <InputLabel htmlFor="phone">Phone</InputLabel>
            <Input id="phone" aria-describedby="phone" />
          </FormControl>
          <div className="button-form-submit">
            <Button variant="contained" color="primary">
              Send
            </Button>
          </div>
        </Container>
        <Container>

        </Container>
      </Container>
    </div>
  );
}

export default App;
