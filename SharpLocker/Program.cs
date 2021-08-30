//Don't Touch Anything Here!!!
﻿using System;
using System.Windows.Forms;

namespace SharpLocker
{
    public static class Program
    {
        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [STAThread]
        public static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new LockScreenForm());

            Application.Run(new LockScreenForm());
        }


    }
}
