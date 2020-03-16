
### fact

```bash
function extract()
{
  if [ -f $1 ] ; then
      case $1 in
          *.tar.bz2)   tar xvjf $1     ;;
          *.tar.gz)    tar xvzf $1     ;;
          *.bz2)       bunzip2 $1      ;;
          *.rar)       unrar x $1      ;;
          *.gz)        gunzip $1       ;;
          *.tar)       tar xvf $1      ;;
          *.tbz2)      tar xvjf $1     ;;
          *.tgz)       tar xvzf $1     ;;
          *.zip)       unzip $1        ;;
          *.Z)         uncompress $1   ;;
          *.7z)        7z x $1         ;;
          *)           echo "'$1' cannot be extracted via >extract<" ;;
      esac
  else
      echo "'$1' is not a valid file!"
  fi
}
```

### fact

https://github.com/yaroslavvb/tensorflow-community-wheels


### fact

Steps to change the default location.

Step 1. Stop docker daemon.

```/etc/init.d/docker stop```

Step 2. Make sure that there are no docker related processes.

```ps aux|grep docker```

Step 3. Move the contents of /var/lib/docker to your new location.

```mv /var/lib/docker /home/```

Step 4. Create a softlink to default location.

```ln -s /home/docker/ /var/lib/docker```

Step 5. Start docker daemon.

```/etc/init.d/docker start```

Step 6. Make sure all the images and data are working from the new location.
