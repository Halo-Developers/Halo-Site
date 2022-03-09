import React, { Component } from 'react';
import { AppBar, Toolbar, Typography } from '@material-ui/core';

class MenuApp extends Component {
    state = {  } 
    render() { 
        return (
            <AppBar position="fixed" color="primary">
              <Toolbar>
                <Typography variant="h6">
                  HalloDev
                </Typography>
              </Toolbar>
            </AppBar>
        );
    }
}
 
export default MenuApp;