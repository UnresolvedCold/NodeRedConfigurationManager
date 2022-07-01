# Nodered Configuration Changer

This small utility helps you to change the current configuration of your node-red app.
With this you can create a new separate environment for different projects.

## How to do it?

1. Copy all the files from the repository and place it in your node-red root directory. For Ubuntu the default root directory is `~/.node-red/`

1. Add an alias to your `~/.bashrc` file referencing the `changeNoderedProfile.sh` file.

    ```bash
        alias node-red-settings="bash ~/.node-red/changeNoderedProfile.sh"
    ```

1. Now you can just create or switch to a new setting by running the utility `node-red-settings`

    ```bash
        # This will create a new flow called 'newFlow' if it does not exist and then switch to this flow.
        # Else it will switch to an exixting flow.
        node-red-settings newFlow && node-red
    ```
