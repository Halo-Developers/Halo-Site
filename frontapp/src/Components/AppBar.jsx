import React from 'react'
import {AppBar} from '@material-ui/core'
import {Toolbar} from '@material-ui/core'
import {Typography} from '@material-ui/core'

export default function PrimaryAppBar() {
  return (
    <div>
        <AppBar position="fixed" color="primary">
          <Toolbar>
            <Typography variant="h6">
              APPBAR
            </Typography>
          </Toolbar>
        </AppBar>
    </div>
  )
}
