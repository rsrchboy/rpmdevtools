(defvar rpmdev-packager-mail-address nil)

(defun rpmdev-packager-mail-address ()
  "Get packager mail address from ~/.fedora.cert."
  (if rpmdev-packager-mail-address
       rpmdev-packager-mail-address
    (let ((certfile (expand-file-name "~/.fedora.cert")))
      (if (file-readable-p certfile)
          (let ((email (shell-command-to-string
                        (format
                         "openssl x509 -noout -email -in %s 2>/dev/null"
                         (shell-quote-argument certfile)))))
            (if email
                (setq rpmdev-packager-mail-address
                      (replace-regexp-in-string "\n.*" "" email))))))
    (unless rpmdev-packager-mail-address
      (setq rpmdev-packager-mail-address ""))
    rpmdev-packager-mail-address))

(defun rpmdev-new-rpm-spec-file-init ()
  (delete-region (point-min) (point-max))
  (set (make-local-variable 'buffer-file-coding-system) 'utf-8)
  (if buffer-file-name
      (call-process "rpmdev-newspec" nil t nil "-o" "-" buffer-file-name)
    (call-process "rpmdev-newspec" nil t nil "-o" "-"))
  (and indent-tabs-mode (tabify (point-min) (point-max)))
  (goto-char (point-min))
  (re-search-forward "^[A-Za-z]+:\\s-*$" nil t)
  (set-buffer-modified-p nil)
  (unless rpm-spec-user-mail-address
    (set (make-local-variable 'rpm-spec-user-mail-address)
         (rpmdev-packager-mail-address))))

(remove-hook 'rpm-spec-mode-new-file-hook 'rpm-spec-initialize)
(add-hook 'rpm-spec-mode-new-file-hook 'rpmdev-new-rpm-spec-file-init t)
